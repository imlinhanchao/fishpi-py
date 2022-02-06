import json
from .__fishpi__ import Base, DOMAIN


class Emoji(Base):

    @property
    def default():
        return {
            "doge": "https://cdn.jsdelivr.net/npm/vditor@3.8.7/dist/images/emoji/doge.png",
            "trollface": "https://cdn.jsdelivr.net/npm/vditor@3.8.7/dist/images/emoji/trollface.png",
            "huaji": "https://cdn.jsdelivr.net/npm/vditor@3.8.7/dist/images/emoji/huaji.gif",
            "octocat": "https://cdn.jsdelivr.net/npm/vditor@3.8.7/dist/images/emoji/octocat.png",
            "wulian": "https://cdn.jsdelivr.net/npm/vditor@3.8.7/dist/images/emoji/wulian.png",
            "smile": f'https://{DOMAIN}/emoji/graphics/smile.png',
            "laughing": f'https://{DOMAIN}/emoji/graphics/laughing.png',
            "blush": f'https://{DOMAIN}/emoji/graphics/blush.png',
            "smiley": f'https://{DOMAIN}/emoji/graphics/smiley.png',
            "relaxed": f'https://{DOMAIN}/emoji/graphics/relaxed.png',
            "smirk": f'https://{DOMAIN}/emoji/graphics/smirk.png',
            "heart_eyes": f'https://{DOMAIN}/emoji/graphics/heart_eyes.png',
            "kissing_heart": f'https://{DOMAIN}/emoji/graphics/kissing_heart.png',
            "kissing_closed_eyes": f'https://{DOMAIN}/emoji/graphics/kissing_closed_eyes.png',
            "flushed": f'https://{DOMAIN}/emoji/graphics/flushed.png',
            "relieved": f'https://{DOMAIN}/emoji/graphics/relieved.png',
            "satisfied": f'https://{DOMAIN}/emoji/graphics/satisfied.png',
            "grin": f'https://{DOMAIN}/emoji/graphics/grin.png',
            "wink": f'https://{DOMAIN}/emoji/graphics/wink.png',
            "stuck_out_tongue_winking_eye": f'https://{DOMAIN}/emoji/graphics/stuck_out_tongue_winking_eye.png',
            "stuck_out_tongue_closed_eyes": f'https://{DOMAIN}/emoji/graphics/stuck_out_tongue_closed_eyes.png',
            "grinning": f'https://{DOMAIN}/emoji/graphics/grinning.png',
            "kissing": f'https://{DOMAIN}/emoji/graphics/kissing.png',
            "kissing_smiling_eyes": f'https://{DOMAIN}/emoji/graphics/kissing_smiling_eyes.png',
            "stuck_out_tongue": f'https://{DOMAIN}/emoji/graphics/stuck_out_tongue.png',
            "sleeping": f'https://{DOMAIN}/emoji/graphics/sleeping.png',
            "worried": f'https://{DOMAIN}/emoji/graphics/worried.png',
            "frowning": f'https://{DOMAIN}/emoji/graphics/frowning.png',
            "anguished": f'https://{DOMAIN}/emoji/graphics/anguished.png',
            "open_mouth": f'https://{DOMAIN}/emoji/graphics/open_mouth.png',
            "grimacing": f'https://{DOMAIN}/emoji/graphics/grimacing.png',
            "confused": f'https://{DOMAIN}/emoji/graphics/confused.png',
            "hushed": f'https://{DOMAIN}/emoji/graphics/hushed.png',
            "expressionless": f'https://{DOMAIN}/emoji/graphics/expressionless.png',
            "unamused": f'https://{DOMAIN}/emoji/graphics/unamused.png',
            "sweat_smile": f'https://{DOMAIN}/emoji/graphics/sweat_smile.png',
            "sweat": f'https://{DOMAIN}/emoji/graphics/sweat.png',
            "disappointed_relieved": f'https://{DOMAIN}/emoji/graphics/disappointed_relieved.png',
            "weary": f'https://{DOMAIN}/emoji/graphics/weary.png',
            "pensive": f'https://{DOMAIN}/emoji/graphics/pensive.png',
            "disappointed": f'https://{DOMAIN}/emoji/graphics/disappointed.png',
            "confounded": f'https://{DOMAIN}/emoji/graphics/confounded.png',
            "fearful": f'https://{DOMAIN}/emoji/graphics/fearful.png',
            "cold_sweat": f'https://{DOMAIN}/emoji/graphics/cold_sweat.png',
            "persevere": f'https://{DOMAIN}/emoji/graphics/persevere.png',
            "cry": f'https://{DOMAIN}/emoji/graphics/cry.png',
            "sob": f'https://{DOMAIN}/emoji/graphics/sob.png',
            "joy": f'https://{DOMAIN}/emoji/graphics/joy.png',
            "astonished": f'https://{DOMAIN}/emoji/graphics/astonished.png',
            "scream": f'https://{DOMAIN}/emoji/graphics/scream.png',
            "tired_face": f'https://{DOMAIN}/emoji/graphics/tired_face.png',
            "angry": f'https://{DOMAIN}/emoji/graphics/angry.png',
            "rage": f'https://{DOMAIN}/emoji/graphics/rage.png',
            "triumph": f'https://{DOMAIN}/emoji/graphics/triumph.png',
            "sleepy": f'https://{DOMAIN}/emoji/graphics/sleepy.png',
            "yum": f'https://{DOMAIN}/emoji/graphics/yum.png',
            "mask": f'https://{DOMAIN}/emoji/graphics/mask.png',
            "sunglasses": f'https://{DOMAIN}/emoji/graphics/sunglasses.png',
            "dizzy_face": f'https://{DOMAIN}/emoji/graphics/dizzy_face.png',
            "imp": f'https://{DOMAIN}/emoji/graphics/imp.png',
            "smiling_imp": f'https://{DOMAIN}/emoji/graphics/smiling_imp.png',
            "neutral_face": f'https://{DOMAIN}/emoji/graphics/neutral_face.png',
            "no_mouth": f'https://{DOMAIN}/emoji/graphics/no_mouth.png',
            "innocent": f'https://{DOMAIN}/emoji/graphics/innocent.png',
            "alien": f'https://{DOMAIN}/emoji/graphics/alien.png',
            "yellow_heart": f'https://{DOMAIN}/emoji/graphics/yellow_heart.png',
            "blue_heart": f'https://{DOMAIN}/emoji/graphics/blue_heart.png',
            "purple_heart": f'https://{DOMAIN}/emoji/graphics/purple_heart.png',
            "heart": f'https://{DOMAIN}/emoji/graphics/heart.png',
            "green_heart": f'https://{DOMAIN}/emoji/graphics/green_heart.png',
            "broken_heart": f'https://{DOMAIN}/emoji/graphics/broken_heart.png',
            "heartbeat": f'https://{DOMAIN}/emoji/graphics/heartbeat.png',
            "heartpulse": f'https://{DOMAIN}/emoji/graphics/heartpulse.png',
            "two_hearts": f'https://{DOMAIN}/emoji/graphics/two_hearts.png',
            "revolving_hearts": f'https://{DOMAIN}/emoji/graphics/revolving_hearts.png',
            "cupid": f'https://{DOMAIN}/emoji/graphics/cupid.png',
            "sparkling_heart": f'https://{DOMAIN}/emoji/graphics/sparkling_heart.png',
            "sparkles": f'https://{DOMAIN}/emoji/graphics/sparkles.png',
            "star": f'https://{DOMAIN}/emoji/graphics/star.png',
            "star2": f'https://{DOMAIN}/emoji/graphics/star2.png',
            "dizzy": f'https://{DOMAIN}/emoji/graphics/dizzy.png',
            "boom": f'https://{DOMAIN}/emoji/graphics/boom.png',
            "collision": f'https://{DOMAIN}/emoji/graphics/collision.png',
            "anger": f'https://{DOMAIN}/emoji/graphics/anger.png',
            "exclamation": f'https://{DOMAIN}/emoji/graphics/exclamation.png',
            "question": f'https://{DOMAIN}/emoji/graphics/question.png',
            "grey_exclamation": f'https://{DOMAIN}/emoji/graphics/grey_exclamation.png',
            "grey_question": f'https://{DOMAIN}/emoji/graphics/grey_question.png',
            "zzz": f'https://{DOMAIN}/emoji/graphics/zzz.png',
            "dash": f'https://{DOMAIN}/emoji/graphics/dash.png',
            "sweat_drops": f'https://{DOMAIN}/emoji/graphics/sweat_drops.png',
            "notes": f'https://{DOMAIN}/emoji/graphics/notes.png',
            "musical_note": f'https://{DOMAIN}/emoji/graphics/musical_note.png',
            "fire": f'https://{DOMAIN}/emoji/graphics/fire.png',
            "poop": f'https://{DOMAIN}/emoji/graphics/poop.png',
            "+1": f'https://{DOMAIN}/emoji/graphics/%2B1.png',
            "thumbsup": f'https://{DOMAIN}/emoji/graphics/thumbsup.png',
            "-1": f'https://{DOMAIN}/emoji/graphics/-1.png',
            "thumbsdown": f'https://{DOMAIN}/emoji/graphics/thumbsdown.png',
            "ok_hand": f'https://{DOMAIN}/emoji/graphics/ok_hand.png',
            "punch": f'https://{DOMAIN}/emoji/graphics/punch.png',
            "facepunch": f'https://{DOMAIN}/emoji/graphics/facepunch.png',
            "fist": f'https://{DOMAIN}/emoji/graphics/fist.png',
            "v": f'https://{DOMAIN}/emoji/graphics/v.png',
            "wave": f'https://{DOMAIN}/emoji/graphics/wave.png',
            "hand": f'https://{DOMAIN}/emoji/graphics/hand.png',
            "raised_hand": f'https://{DOMAIN}/emoji/graphics/raised_hand.png',
            "open_hands": f'https://{DOMAIN}/emoji/graphics/open_hands.png',
            "point_up": f'https://{DOMAIN}/emoji/graphics/point_up.png',
            "point_down": f'https://{DOMAIN}/emoji/graphics/point_down.png',
            "point_left": f'https://{DOMAIN}/emoji/graphics/point_left.png',
            "point_right": f'https://{DOMAIN}/emoji/graphics/point_right.png',
            "raised_hands": f'https://{DOMAIN}/emoji/graphics/raised_hands.png',
            "pray": f'https://{DOMAIN}/emoji/graphics/pray.png',
            "point_up_2": f'https://{DOMAIN}/emoji/graphics/point_up_2.png',
            "clap": f'https://{DOMAIN}/emoji/graphics/clap.png',
            "muscle": f'https://{DOMAIN}/emoji/graphics/muscle.png',
            "couple": f'https://{DOMAIN}/emoji/graphics/couple.png',
            "family": f'https://{DOMAIN}/emoji/graphics/family.png',
            "two_men_holding_hands": f'https://{DOMAIN}/emoji/graphics/two_men_holding_hands.png',
            "two_women_holding_hands": f'https://{DOMAIN}/emoji/graphics/two_women_holding_hands.png',
            "dancer": f'https://{DOMAIN}/emoji/graphics/dancer.png',
            "dancers": f'https://{DOMAIN}/emoji/graphics/dancers.png',
            "ok_woman": f'https://{DOMAIN}/emoji/graphics/ok_woman.png',
            "no_good": f'https://{DOMAIN}/emoji/graphics/no_good.png',
            "information_desk_person": f'https://{DOMAIN}/emoji/graphics/information_desk_person.png',
            "raising_hand": f'https://{DOMAIN}/emoji/graphics/raising_hand.png',
            "bride_with_veil": f'https://{DOMAIN}/emoji/graphics/bride_with_veil.png',
            "person_with_pouting_face": f'https://{DOMAIN}/emoji/graphics/person_with_pouting_face.png',
            "person_frowning": f'https://{DOMAIN}/emoji/graphics/person_frowning.png',
            "bow": f'https://{DOMAIN}/emoji/graphics/bow.png',
            "couplekiss": f'https://{DOMAIN}/emoji/graphics/couplekiss.png',
            "couple_with_heart": f'https://{DOMAIN}/emoji/graphics/couple_with_heart.png',
            "massage": f'https://{DOMAIN}/emoji/graphics/massage.png',
            "haircut": f'https://{DOMAIN}/emoji/graphics/haircut.png',
            "nail_care": f'https://{DOMAIN}/emoji/graphics/nail_care.png',
            "boy": f'https://{DOMAIN}/emoji/graphics/boy.png',
            "girl": f'https://{DOMAIN}/emoji/graphics/girl.png',
            "woman": f'https://{DOMAIN}/emoji/graphics/woman.png',
            "man": f'https://{DOMAIN}/emoji/graphics/man.png',
            "baby": f'https://{DOMAIN}/emoji/graphics/baby.png',
            "older_woman": f'https://{DOMAIN}/emoji/graphics/older_woman.png',
            "older_man": f'https://{DOMAIN}/emoji/graphics/older_man.png',
            "person_with_blond_hair": f'https://{DOMAIN}/emoji/graphics/person_with_blond_hair.png',
            "man_with_gua_pi_mao": f'https://{DOMAIN}/emoji/graphics/man_with_gua_pi_mao.png',
            "man_with_turban": f'https://{DOMAIN}/emoji/graphics/man_with_turban.png',
            "construction_worker": f'https://{DOMAIN}/emoji/graphics/construction_worker.png',
            "cop": f'https://{DOMAIN}/emoji/graphics/cop.png',
            "angel": f'https://{DOMAIN}/emoji/graphics/angel.png',
            "princess": f'https://{DOMAIN}/emoji/graphics/princess.png',
            "smiley_cat": f'https://{DOMAIN}/emoji/graphics/smiley_cat.png',
            "smile_cat": f'https://{DOMAIN}/emoji/graphics/smile_cat.png',
            "heart_eyes_cat": f'https://{DOMAIN}/emoji/graphics/heart_eyes_cat.png',
            "kissing_cat": f'https://{DOMAIN}/emoji/graphics/kissing_cat.png',
            "smirk_cat": f'https://{DOMAIN}/emoji/graphics/smirk_cat.png',
            "scream_cat": f'https://{DOMAIN}/emoji/graphics/scream_cat.png',
            "crying_cat_face": f'https://{DOMAIN}/emoji/graphics/crying_cat_face.png',
            "joy_cat": f'https://{DOMAIN}/emoji/graphics/joy_cat.png',
            "pouting_cat": f'https://{DOMAIN}/emoji/graphics/pouting_cat.png',
            "japanese_ogre": f'https://{DOMAIN}/emoji/graphics/japanese_ogre.png',
            "japanese_goblin": f'https://{DOMAIN}/emoji/graphics/japanese_goblin.png',
            "see_no_evil": f'https://{DOMAIN}/emoji/graphics/see_no_evil.png',
            "hear_no_evil": f'https://{DOMAIN}/emoji/graphics/hear_no_evil.png',
            "speak_no_evil": f'https://{DOMAIN}/emoji/graphics/speak_no_evil.png',
            "guardsman": f'https://{DOMAIN}/emoji/graphics/guardsman.png',
            "skull": f'https://{DOMAIN}/emoji/graphics/skull.png',
            "feet": f'https://{DOMAIN}/emoji/graphics/feet.png',
            "lips": f'https://{DOMAIN}/emoji/graphics/lips.png',
            "kiss": f'https://{DOMAIN}/emoji/graphics/kiss.png',
            "droplet": f'https://{DOMAIN}/emoji/graphics/droplet.png',
            "ear": f'https://{DOMAIN}/emoji/graphics/ear.png',
            "eyes": f'https://{DOMAIN}/emoji/graphics/eyes.png',
            "nose": f'https://{DOMAIN}/emoji/graphics/nose.png',
            "tongue": f'https://{DOMAIN}/emoji/graphics/tongue.png',
            "love_letter": f'https://{DOMAIN}/emoji/graphics/love_letter.png',
            "bust_in_silhouette": f'https://{DOMAIN}/emoji/graphics/bust_in_silhouette.png',
            "busts_in_silhouette": f'https://{DOMAIN}/emoji/graphics/busts_in_silhouette.png',
            "speech_balloon": f'https://{DOMAIN}/emoji/graphics/speech_balloon.png',
            "thought_balloon": f'https://{DOMAIN}/emoji/graphics/thought_balloon.png'
        }

    def get(self):
        """获取用户自定义表情"""
        if self.apiKey == '':
            return []
        return json.loads(self.json('/api/cloud/get', {
            'gameId': 'emojis',
            'apiKey': self.apiKey
        })['data'])

    def set(self, emojis: list):
        """查询登录用户当前活跃度，请求频率请控制在 30 ~ 60 秒一次"""
        if self.apiKey == '':
            return None
        return self.json('/api/cloud/sync', {
            'gameId': 'emojis',
            'apiKey': self.apiKey,
            'data': json.dumps(emojis)
        })
